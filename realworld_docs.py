import io
import requests
import frontmatter
import zipfile

def read_repo(repo_author, repo_name):
    domain = 'https://github.com'
    url = f'{domain}/{repo_author}/{repo_name}/archive/refs/heads/main.zip'
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception('Failed to download repo content '+ response.status_code)
    
    repository_data = []
    zf = zipfile.ZipFile(io.BytesIO(response.content))

    for file_info in zf.infolist():
        filename = file_info.filename.lower()

        if not (filename.endswith('.md') or filename.endswith('.mdx')):
            continue

        try:
            with zf.open(file_info) as f_in:
                content = f_in.read().decode('utf-8', errors='ignore')
                posts = frontmatter.loads(content)
                data = posts.to_dict()
                data['filename'] = filename
                repository_data.append(data)
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            continue
    zf.close()
    return repository_data