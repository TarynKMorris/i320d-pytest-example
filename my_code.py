import pytest
import re

def fix_phone_num(phone_num_to_fix):
  phone_num_to_fix = re.sub('[()-]','', phone_num_to_fix)
  phone_num_to_fix = phone_num_to_fix.replace(" ","")
  # can only handle numbers that are exactly 10 digits long
  if (len(phone_num_to_fix) != 10):
    raise ValueError("Can only format numbers that are exactly 10 digits long")
  if (not phone_num_to_fix.isdigit()):
    raise ValueError("Cannot accept non-digits")
  
  # given "5125558823". Split the parts, then recombine and return
  area_code = phone_num_to_fix[0:3] # 512 (first three digits)
  three_part = phone_num_to_fix[3:6] # 555 (next three digits)
  four_part = phone_num_to_fix[6:] # # 8823 (last four digits)
  
  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
  
  return fixed_num

def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
  assert fix_phone_num("5554429876") == '(555) 442 9876'
  assert fix_phone_num("3216543333") == '(321) 654 3333'

def test_phone_num_length():
  with pytest.raises(ValueError):
    fix_phone_num("51")

def test_all_digit():
  with pytest.raises(ValueError):
    fix_phone_num("555442abcd")

def test_additional_phone_num_formats():
  with pytest.raises(ValueError):
    fix_phone_num("555-442-98761")
  assert fix_phone_num("(321) 654 3333") == '(321) 654 3333'
