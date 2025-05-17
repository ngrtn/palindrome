def reset():
    cmnd = str(input('Do you want to start again? y/n\n'))
    if cmnd == 'y':
        print('Restarting...')
        main()
    if cmnd == 'n':
        print()

def main():
    pal = str(input('\nThis is Palindrome checker. To start type word or sentence below!\n')) # pal == palindrome
    rev = pal[::-1] # rev == reversed
    if rev == pal:
        print('This is palindrome!')
        reset()
    else:
        print('This is not palidrome. Your result:', rev)
        reset()
main()