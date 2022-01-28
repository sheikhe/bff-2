if __name__=='__main__':
    try:
        __import__("cr").menu()
    except Exception as e:
        exit(str(e))
