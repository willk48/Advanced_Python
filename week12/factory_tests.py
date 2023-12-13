import pytest
import factory_v2

def shirt(v=False):
    if (v==False):
        return S_TIME
    else:
        print("Starting:  t_shirt...")
        print("Completed: t_shirt.")
        return S_TIME

def pants(v=False):
    if (v==False):
        return P_TIME
    else:
        print("Starting:  pants...")
        print("Completed: pants.")
        return P_TIME

def hat(v=False):
    if (v==False):
        return H_TIME
    else:
        print("Starting:  hat...")
        print("Completed: hat. ☻")
        return H_TIME

def half_list(a_list):
    len_half = len(a_list)//2
    return a_list[:len_half], a_list[len_half:]

def test_clothing_items():
    assert factory_v2.shirt()==0.4
    assert factory_v2.pants()==0.9
    assert factory_v2.hat()==0.5

def test_half_list():
    lst = [1,2,3,4,5,6,7,8]
    assert half_list(lst)==([1,2,3,4],[5,6,7,8])