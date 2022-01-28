if __name__=='__main__':
    try:
        __import__("crack").menu()
    except Exception as e:
        exit(str(e))
