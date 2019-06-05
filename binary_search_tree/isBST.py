"""
Assume Node() is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

runtime: O(n)
author: Manish Suthar
"""

def check_binary_search_tree_(root, mini=-99999999, maxi=99999999):

    if not root:
        return True
    if root.data <= mini or root.data >= maxi:
        return False

    return check_binary_search_tree_(root.left, mini, root.data) and \
        check_binary_search_tree_(root.right, root.data, maxi)
