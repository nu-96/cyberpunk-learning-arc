import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from linked_list import LinkedList


@pytest.fixture
def ll():
    li = LinkedList()
    li.append(1)
    li.append(2)
    li.append(3)
    li.append(4)
    return li


def test_length(ll):
    assert ll.length == 4

def test_append(ll):
    assert ll.nhead.value == 1
    assert ll.nlast.value == 4

def test_delete_middle(ll):
    ll.delete(1)
    assert ll.length == 3


def test_delete_middle_harder(ll, capsys):
    ll.delete(2)
    print(ll)
    captured = capsys.readouterr()
    assert captured.out == "1 -> 2 -> 4\n"

def test_delete_head(ll):
    ll.delete(0)
    assert ll.nhead.value == 2

def test_delete_tail(ll):
    ll.delete(3)
    assert ll.nlast.value == 3

def test_search(ll):
    assert ll.search(0) == 1