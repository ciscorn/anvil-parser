import context as _
from anvil import RORegion
import io
import secrets

def test_from_filename(tmp_path):
    filename = tmp_path / "region.mca"
    contents = secrets.token_bytes()

    with open(filename, 'wb') as f:
        f.write(contents)

    region = RORegion.from_file(str(filename))
    assert region.data == contents

def test_from_filelike():
    contents = secrets.token_bytes()
    filelike = io.BytesIO(contents)

    region = RORegion.from_file(filelike)
    assert region.data == contents
