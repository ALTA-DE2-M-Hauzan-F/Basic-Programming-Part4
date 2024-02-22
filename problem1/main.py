def play_with_asterisk(n):
    pattern = ""
    for i in range(n):
        for sp in range(n-i):
            if sp ==n-i-1:
                # ganti end="" (no spasi di ujung row)
                pattern +=""
            else:pattern +=" "
        for j in range(i+1):
            pattern +="* "
        pattern +="\n"
    return pattern

if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """
