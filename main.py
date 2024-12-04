with open('sample-1.txt') as doc:
    content = doc.read()
    words = content.split()
    word_count = len(words) if content else 0
    letter_count = len(content) if content else 0
    
    
    print(f"Word count: {word_count}")
    print(f"Letter count: {letter_count}")
    print(content)
