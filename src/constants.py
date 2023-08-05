

CARDS = ['line', 'type', 'size', 'stat', 'char', 'star', 'cmit']

NON_TEXT_TYPE = [

    ## Images
    '.jpg', '.jpeg', '.png', '.gif',

    ## Videos
    '.mp4',

    ## Audios
    '.mp3',

    ## .git/
    '.idx', '.pack', '.rev',
]
NON_TEXT_FILENAME = [

    ## .git/
    'index',
]

TYPE_TO_NAME = {
    '.py': 'Python',
    '.js': 'JavaScript',
    '.java': 'Java',
    '.cpp': 'C++',
    '.html': 'HTML',
    '.css': 'CSS',
    '.rb': 'Ruby',
    '.php': 'PHP',
    '.swift': 'Swift',
    '.kt': 'Kotlin',
    '.pl': 'Perl',
    '.sh': 'Shell',
    '.xml': 'XML',
    '.json': 'JSON',
    '.sql': 'SQL',
    '.md': 'Markdown',
    '.txt': 'Plain Text',
    '.c': 'C',
    '.h': 'C Header',
    '.pyc': 'Python Compiled File',
    '.jar': 'Java Archive',
    '.exe': 'Executable',
    '.dll': 'Dynamic Link Library',
    '.ppt': 'PowerPoint',
    '.pdf': 'PDF',
    '.jpg': 'JPEG Image',
    '.png': 'PNG Image',
    '.mp3': 'MP3 Audio',
    '.mp4': 'MP4 Video',
}