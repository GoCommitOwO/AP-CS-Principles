def main():
    word = input("gimmie yo word\n")
    word = word.lower()
    dblcount = 0
    for lcv in range(0, len(word) - 1):
        if word[lcv] == word[lcv + 1]:
            dblcount += 1
    print(f"there are " + str(dblcount) + " double letters in" + word)


if __name__ == "__main__":
    main()