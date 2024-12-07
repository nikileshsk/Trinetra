import unittest
from app import (
    is_valid_url,
    check_safe_browsing,
    verify_ssl_cert,
    analyze_url
)

class TestURLFunctions(unittest.TestCase):
    def test_url_validation(self):
        # Test valid URLs
        self.assertTrue(is_valid_url("https://www.example.com"))
        self.assertTrue(is_valid_url("http://example.com"))
        self.assertTrue(is_valid_url("ftp://example.com"))

        # Test invalid URLs
        self.assertFalse(is_valid_url("not a valid url"))
        self.assertFalse(is_valid_url("example.com"))

    def test_safe_browsing_check(self):
        # Test safe URLs
        self.assertEqual(check_safe_browsing("https://www.google.com"), "Safe")

        # Test potentially unsafe URLs
        self.assertNotEqual(check_safe_browsing("https://phishing.example.com"), "Safe")

    def test_ssl_certificate_validation(self):
        # Test valid SSL certificate
        self.assertEqual(verify_ssl_cert("https://www.google.com"), "Valid")

        # Test invalid SSL certificate (if possible)

    def test_url_analysis(self):
        # Test safe URLs
        self.assertEqual(analyze_url("https://www.wikipedia.org"), "Safe")

        # Test suspicious URLs
        self.assertNotEqual(analyze_url("https://www.phishing.example.com"), "Safe")

if __name__ == '__main__':
    unittest.main()
