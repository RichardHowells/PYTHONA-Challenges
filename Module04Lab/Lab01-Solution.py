

This is not right yet!!!

def parenSeeker(text, startPoint):
    currentCh = startPoint
    while currentCh < len(text):
        openText = ''

        #  Handle parenthesized sub text
        if text[currentCh] == '(':

            #Skip the '('
        
            currentCh += 1
            while currentCh < len(text) and text[currentCh] != ')':
                # Skip forward by the entire parenthesised subtext
                currentCh = parenSeeker(text, currentCh)
            

            # Skip the ')'
            currentCh +=1
        
        # Unparenthesized char
        openText += text[currentCh]
        
        currentCh += 1

    print("Open text = ", openText)

    return currentCh

text = "abc (zyx) (wvu) def"
print("Scanning", text)
parenSeeker(text, 0)

text = "abc (zyx (def) wv) ghi"
print("Scanning ", text)
parenSeeker(text, 0)
