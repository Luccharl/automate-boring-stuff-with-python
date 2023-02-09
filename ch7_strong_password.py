import re

def detect_strong_pass(password):
    strong_pass = re.compile(r'''(
                        ^(?=.*[A-Z])                # at least one uppercase letter
                        (?=.*[!@#$&*])              # at least one special character
                        (?=.*[0-9].*[0-9])          # at least two numeric digits
                        (?=.*[a-z].*[a-z])          # at least two lowercase letters
                        .{8,}                       # at least 8 total digits
                        $)''', re.VERBOSE)
    
    matched_obj = strong_pass.search(password)
    
    if matched_obj is None:
        print('It is not a valid password')
        return False
    else:   
        print('It is a valid password')
        return True

            
detect_strong_pass('ZZasda1233444@')