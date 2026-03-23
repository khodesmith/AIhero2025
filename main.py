from realworld_docs import read_repo

def main():
    realworld = read_repo('realworld-apps', 'realworld')
    print(f"FAQ documents: {len(realworld)}")
    # for doc in realworld:
    #     print(doc['filename'])
    print(realworld[7])


if __name__ == "__main__":
    main()
