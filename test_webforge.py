# test_webforge.py
"""
Tests for WebForge module.
"""

import unittest
from webforge import WebForge

class TestWebForge(unittest.TestCase):
    """Test cases for WebForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WebForge()
        self.assertIsInstance(instance, WebForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WebForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
