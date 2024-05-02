import unittest
canUnlockAll = __import__('0-lockboxes').canUnlockAll

class TestLockBoxes(unittest.TestCase):
    def test_empty_boxes(self):
        boxes = []
        self.assertTrue(canUnlockAll(boxes))

    def test_single_box(self):
        boxes = [[1, 2, 3]]
        self.assertTrue(canUnlockAll(boxes))

    def test_multiple_boxes_unlocked(self):
        boxes = [[1], [2], [3], []]
        self.assertTrue(canUnlockAll(boxes))

    def test_multiple_boxes_not_unlocked(self):
        boxes = [[1], [2], [3], []]
        self.assertTrue(canUnlockAll(boxes))

    def test_circular_dependency(self):
        boxes = [[1], [2], [0]]
        self.assertTrue(canUnlockAll(boxes))

    def test_large_boxes(self):
        boxes = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
        self.assertTrue(canUnlockAll(boxes))

if __name__ == '__main__':
  unittest.main()
