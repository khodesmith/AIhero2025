from realworld_docs import read_repo, sliding_window, split_markdown_by_level

def main():
    realworld = read_repo('realworld-apps', 'realworld')
    print(f"FAQ documents: {len(realworld)}")
    for doc in realworld:
        print(doc['filename'])
    print(realworld[1])
    for i, doc in enumerate(realworld):
        print(f"Doc {i}: {len(doc['content'])} document in {doc['filename']}")


    realworld_chunks = []
    for doc in realworld:
        doc_copy = doc.copy()
        doc_content = doc_copy.pop('content')
        chunks = sliding_window(doc_content, 2000,1000)
        for chunk in chunks:
            chunk.update(doc_copy)
        realworld_chunks.extend(chunks)

    realworld_section_chunks = []

    for doc in realworld:
        doc_copy = doc.copy()
        doc_content = doc_copy.pop('content')
        sections = split_markdown_by_level(doc_content, level=2)
        for section in sections:
            section_doc = doc_copy.copy()
            section_doc['section'] = section
            realworld_section_chunks.append(section_doc)
    
    print(realworld_section_chunks[23])


if __name__ == "__main__":
    main()
