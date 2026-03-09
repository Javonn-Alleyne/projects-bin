import unicodedata
import base64
import zlib
from typing import List, Tuple, Optional

class ReversibleTriEncoder:
    """
    A reversible encoding system that produces human-readable TRI-tags
    while maintaining the ability to decode back to original input.
    """
    
    def __init__(self):
        # Base85 alphabet for compact encoding (excludes confusing chars)
        self.b85_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"
        
    def normalize_input(self, text: str) -> str:
        """Normalize unicode and clean input"""
        normalized = unicodedata.normalize("NFKD", text)
        return "".join(ch for ch in normalized if not unicodedata.combining(ch))
    
    def generate_tri_tag(self, text: str) -> str:
        """Generate a 3-letter tag from text using your original algorithm"""
        # Use your existing A1Z26 + binary chunking approach for the tag
        nums = []
        text_norm = self.normalize_input(text)
        
        for ch in text_norm:
            if ch.isalpha():
                nums.append(f"{ord(ch.upper())-64:02d}")
        
        if not nums:
            return "XXX"
            
        concat_num = "".join(nums)
        binary = bin(int(concat_num))[2:] if concat_num else "0"
        
        # Pad to 5-bit chunks
        pad = (-len(binary)) % 5
        binary = ("0" * pad) + binary
        chunks = [binary[i:i+5] for i in range(0, len(binary), 5)]
        
        # Convert to letters (simplified version of your mapping)
        tag_chars = []
        for chunk in chunks[:3]:  # Take first 3 chunks
            val = int(chunk, 2)
            if 1 <= val <= 26:
                tag_chars.append(chr(ord('A') + val - 1))
            else:
                tag_chars.append('X')
        
        # Ensure exactly 3 characters
        while len(tag_chars) < 3:
            tag_chars.append('X')
            
        return "".join(tag_chars[:3])
    
    def compress_data(self, text: str) -> bytes:
        """Compress the original data for storage"""
        text_bytes = text.encode('utf-8')
        compressed = zlib.compress(text_bytes, level=9)
        return compressed
    
    def encode_payload(self, compressed_data: bytes) -> str:
        """Encode compressed data as a compact string"""
        # Use base64 for now (could optimize with base85 later)
        encoded = base64.b85encode(compressed_data).decode('ascii')
        return encoded
    
    def encode(self, text: str) -> Tuple[str, str]:
        """
        Encode text into a TRI-tag and reversible payload.
        Returns: (tri_tag, payload)
        """
        if not text.strip():
            return "XXX", ""
            
        tri_tag = self.generate_tri_tag(text)
        compressed = self.compress_data(text)
        payload = self.encode_payload(compressed)
        
        return tri_tag, payload
    
    def decode(self, tri_tag: str, payload: str) -> str:
        """
        Decode payload back to original text.
        tri_tag is provided for verification but not needed for decoding.
        """
        if not payload:
            return ""
            
        try:
            compressed_data = base64.b85decode(payload.encode('ascii'))
            text_bytes = zlib.decompress(compressed_data)
            original_text = text_bytes.decode('utf-8')
            
            # Verify the tri_tag matches (optional integrity check)
            expected_tag = self.generate_tri_tag(original_text)
            if tri_tag != expected_tag:
                print(f"Warning: TRI-tag mismatch. Expected: {expected_tag}, Got: {tri_tag}")
            
            return original_text
            
        except Exception as e:
            raise ValueError(f"Failed to decode payload: {e}")
    
    def encode_combined(self, text: str, separator: str = "::") -> str:
        """
        Create a single string containing both TRI-tag and payload.
        Format: TRI::payload
        """
        tri_tag, payload = self.encode(text)
        return f"{tri_tag}{separator}{payload}"
    
    def decode_combined(self, combined: str, separator: str = "::") -> str:
        """Decode from combined format"""
        if separator not in combined:
            raise ValueError(f"Invalid format: separator '{separator}' not found")
        
        tri_tag, payload = combined.split(separator, 1)
        return self.decode(tri_tag, payload)


# Demo and testing functions
def demo_encoder():
    encoder = ReversibleTriEncoder()
    
    test_cases = [
        "SUN",
        "Hello World",
        "This is a longer paragraph with multiple sentences. It should compress well and still be fully recoverable!",
        "François Müller-Smith",  # Unicode test
        "A",  # Single character
        "12345",  # Numbers
        "",  # Empty
        "The quick brown fox jumps over the lazy dog. " * 10  # Long repetitive text
    ]
    
    print("=== Reversible TRI-Tag Encoder Demo ===\n")
    
    for text in test_cases:
        print(f"Original: '{text}'")
        
        if not text:
            print("  (empty input)")
            print()
            continue
            
        try:
            # Encode
            tri_tag, payload = encoder.encode(text)
            combined = encoder.encode_combined(text)
            
            # Decode
            decoded = encoder.decode(tri_tag, payload)
            decoded_combined = encoder.decode_combined(combined)
            
            # Stats
            original_size = len(text.encode('utf-8'))
            payload_size = len(payload)
            combined_size = len(combined)
            compression_ratio = payload_size / original_size if original_size > 0 else 0
            
            print(f"  TRI-tag: {tri_tag}")
            print(f"  Payload: {payload[:50]}{'...' if len(payload) > 50 else ''}")
            print(f"  Combined: {combined[:50]}{'...' if len(combined) > 50 else ''}")
            print(f"  Sizes: {original_size}→{payload_size} bytes ({compression_ratio:.2f} ratio)")
            print(f"  Decode success: {decoded == text and decoded_combined == text}")
            
            if decoded != text:
                print(f"  ERROR: Decoded text doesn't match!")
                print(f"    Expected: '{text}'")
                print(f"    Got: '{decoded}'")
                
        except Exception as e:
            print(f"  ERROR: {e}")
        
        print()

def test_collision_rate():
    """Test how often different inputs produce the same TRI-tag"""
    encoder = ReversibleTriEncoder()
    
    # Generate test data
    test_words = [
        "sun", "moon", "star", "earth", "mars", "venus", "jupiter", "saturn",
        "hello", "world", "python", "code", "test", "demo", "example", "sample",
        "quick", "brown", "fox", "lazy", "dog", "jumps", "over", "the",
        "alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta"
    ]
    
    tag_map = {}
    collisions = 0
    
    for word in test_words:
        tri_tag, _ = encoder.encode(word)
        if tri_tag in tag_map:
            print(f"COLLISION: '{word}' and '{tag_map[tri_tag]}' both map to '{tri_tag}'")
            collisions += 1
        else:
            tag_map[tri_tag] = word
    
    print(f"\nCollision rate: {collisions}/{len(test_words)} ({collisions/len(test_words)*100:.1f}%)")
    print(f"Unique tags: {len(tag_map)}")

if __name__ == "__main__":
    demo_encoder()
    print("\n" + "="*50 + "\n")
    test_collision_rate()