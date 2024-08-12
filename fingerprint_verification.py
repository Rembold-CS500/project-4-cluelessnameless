######################################################################
# Names of any others you worked with:
# Received some help/advice from Hailee & Bryant (Namely my trouble with calling the correct file, then with some of the math for shifted_check)
# Additionally, some use of reddit/google & my notes for certain built-ins (i.e. splitlines(), len, etc.)
# AI transcript if used:
# Any extensions done:
######################################################################

# open and read the file then return the content as a string
def read_print(filename):
    """Reads the given print and returns a dictionary with all info."""
    with open(filename, 'r') as fh:
        # splitlines after read to remove \n
        lines = fh.read().splitlines()
    # the string of characters being the fingerprint
    # currently the "name, width, height" comes according to file
        name = lines[0]
        width = lines[1]
        height = lines[2]
        fingerprint = lines[3:]
    # add to a dictionary
        data = {'name': name, 'width': width, 'height': height,
                'fingerprint': fingerprint}
        return data

# we just want to show a dictionary at the end (like a parsed version of the file)
# showing the comparisons

# simple check if match True, if not False
def simple_check(fingerprint1, fingerprint2):
    if fingerprint1 != fingerprint2:
        return False
    return True

# variant check, if matches/total greater/equal to threshold, True, if not False
def variant_check(fingerprint1, fingerprint2, threshold = .95):
    # matches count number of matching characters with our fingerprints
    # total to count the total number of characters entirely
    matches = 0
    total = 0
    # outer loop for each row, inner to look at characters in each row
    # necessary len for length/character counting
    # calling from fingerprint to set line start
    for i in range(len(fingerprint1['fingerprint'])):
        for j in range(len(fingerprint1['fingerprint'][i])):
            total += 1
            if fingerprint1['fingerprint'][i][j] == fingerprint2['fingerprint'][i][j]:
                matches += 1
    # if it's above the threshold, it's a match
    return (matches / total) >= threshold

# shifted check, still checking the variant, but adjusting for changes in x and y both positive & negative
# max changes should be 5, keeping within the threshold
# max matches will start at 0, similar to variant

def shifted_check(fingerprint1, fingerprint2, threshold = .95):
    max_change = 5
    max_matches = 0

    # adjust for change in x and change in y, loop for up down left right (-/+)
    for dx in range(-max_change, max_change + 1):
        for dy in range(-max_change, max_change + 1):
            matches = 0
            total = 0
            # loop within like variant, checking rows and within rows
            # the change/shift needs to account for the up/down left/right shifts, add change in x/y to the row, then column
            for i in range(len(fingerprint1['fingerprint'])):
                for j in range(len(fingerprint1['fingerprint'][i])):
                    di = i + dy
                    dj = j + dx
                    if 0 <= di < len(fingerprint1['fingerprint']) and 0 <= dj < len(fingerprint1['fingerprint'][i]):
                        if fingerprint1['fingerprint'][i][j] == fingerprint2['fingerprint'][di][dj]:
                            matches += 1
                        total += 1
            
            if total > 0:
                max_matches = max(max_matches, (matches / total))
    return max_matches >= threshold


if __name__ == '__main__':
    # Just to get you started
    #data = read_print("./prints/User1_Original.txt")
    #print(data)

    # lets add some files to call from
    fh1 = './prints/User1_Original.txt'
    fh1_v1 = './prints/User1_Variant1.txt'
    fh1_v2 = './prints/User1_Variant2.txt'
    fh1_shiftedv1 = './prints/User1_ShiftedVariant1.txt'
    fh1_shiftedv2 = './prints/User1_ShiftedVariant2.txt'

    fh2 = './prints/User2_Original.txt'
    fh2_v1 = './prints/User2_Variant1.txt'
    fh2_v2 = './prints/User2_Variant2.txt'
    fh2_shiftedv1 = './prints/User2_ShiftedVariant1.txt'
    fh2_shiftedv2 = './prints/User2_ShiftedVariant2.txt'

    fp1 = read_print(fh1)
    fp1_v1 = read_print(fh1_v1)
    fp1_v2 = read_print(fh1_v2)
    fp1_shiftedv1 = read_print(fh1_shiftedv1)
    fp1_shiftedv2 = read_print(fh1_shiftedv2)

    fp2 = read_print(fh2)
    fp2_v1 = read_print(fh2_v1)
    fp2_v2 = read_print(fh2_v2)
    fp2_shiftedv1 = read_print(fh2_shiftedv1)
    fp2_shiftedv2 = read_print(fh2_shiftedv2)

    # for a simple check
    print("Simple Checks:")
    print(f"Fingerprint match: {simple_check(fp1,fp2)}")
    # expected False
    print(f"Fingerprint match: {simple_check(fp1,fp1)}")
    # expected True
    print("")

    # for a variant check
    print("Variant Checks:")
    print(f"Fingerprint match: {variant_check(fp1, fp1_v1)}")
    # expected True
    print(f"Fingerprint match: {variant_check(fp1, fp1_v2)}")
    # expected True
    print(f"Fingerprint match: {variant_check(fp1_v1, fp1_v2)}")
    # expected True      
    print(f"Fingerprint match: {variant_check(fp1, fp1_shiftedv1)}")
    # expected False
    print(f"Fingerprint match: {variant_check(fp1, fp2)}")
    # expected False
    print("")

    # for a shifted check
    print("Shifted Checks")
    print(f"Fingerprint match: {shifted_check(fp1,fp1_shiftedv1)}")
    # expected True - was returning False but why? - was not including the upper range, +1 fix
    print(f"Fingerprint match: {shifted_check(fp1,fp1_shiftedv2)}")
    # expected True
    print(f"Fingerprint match: {shifted_check(fp1_shiftedv1,fp1_shiftedv2)}")
    # expected True    
    print(f"Fingerprint match: {shifted_check(fp1,fp2)}")
    # expected False
    #print(f"Fingerprint match: {shifted_check(fp2,fp2_shiftedv1)}")
    # expected True
    #print(f"Fingerprint match: {shifted_check(fp2,fp2_shiftedv2)}")
    # expected True
    #print(f"Fingerprint match: {shifted_check(fp2_shiftedv1,fp2_shiftedv2)}")
    # expected True
