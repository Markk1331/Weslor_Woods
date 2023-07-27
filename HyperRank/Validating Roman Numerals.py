regex_pattern = r"^[IVXLCDM]+[IVXLCDM]$"
import re
print(str(bool(re.match(regex_pattern, input()))))