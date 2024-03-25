import pytest
from datetime import datetime

if __name__ == '__main__':
    now = datetime.today().strftime('%Y%m%d_%H%M%S')
    pytest.main(['cases', f'--html=reports/{now}.html', '--self-contained-html'])
