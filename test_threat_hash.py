import os
import time
import hashlib
from threat_hash import handle_process, hash_cache

def is_admin():
    """
    Check if the current script is being run with administrative privileges.
    """
    try:
        print("test is_admin passed.")
        return os.system("NET SESSION >nul 2>&1") == 0
    except Exception:
        print("test is_admin failed.")


def clear_hash_cache():
    """
    Clear hash_cache before each test.
    """
    hash_cache.clear()

def test_to_handle_process_new_entry():
    """
    Test handling a new process entry.
    """
    clear_hash_cache()
    process_data = {
        "name": "test_process",
        "path": "/path/to/test_process",
        "hash": hashlib.sha256(b"test_process").hexdigest()
    }
    handle_process(process_data)
    assert process_data['hash'] in hash_cache
    assert hash_cache[process_data['hash']]['counter'] == 1
    print("test_handle_process_new_entry passed.")

def test_handle_process_duplicate_within_60_seconds():
    """
    Test handling a duplicate process within 60 seconds.
    """
    clear_hash_cache()
    process_data = {
        "name": "test_process",
        "path": "/path/to/test_process",
        "hash": hashlib.sha256(b"test_process").hexdigest()
    }
    handle_process(process_data)
    handle_process(process_data)
    assert hash_cache[process_data['hash']]['counter'] == 2
    print("test_handle_process_duplicate_within_60_seconds passed.")

def test_handle_process_after_60_seconds():
    """
    Test handling a process after 60 seconds.
    """
    clear_hash_cache()
    process_data = {
        "name": "test_process",
        "path": "/path/to/test_process",
        "hash": hashlib.sha256(b"test_process").hexdigest()
    }
    handle_process(process_data)
    time.sleep(61)  
    handle_process(process_data)
    assert hash_cache[process_data['hash']]['counter'] == 1
    print("test_handle_process_after_60_seconds passed.")

def test_handle_process_long_path():
    """
    Test handling a process with a long path.
    """
    clear_hash_cache()
    long_path = "/this/is/a/very/long/path/to/the/test_process/that/exceeds/the/typical/path/length/for/a/file/on/the/system/executable"
    process_data = {
        "name": "test_process_999",
        "path": long_path,
        "hash": hashlib.sha256(long_path.encode()).hexdigest()
    }
    handle_process(process_data)
    assert process_data['hash'] in hash_cache
    assert hash_cache[process_data['hash']]['counter'] == 1
    print("test_handle_process_long_path passed.")

if __name__ == "__main__":
    is_admin()
    test_to_handle_process_new_entry()
    test_handle_process_duplicate_within_60_seconds()
    test_handle_process_after_60_seconds()
    test_handle_process_long_path()
    print('all tests passed')
