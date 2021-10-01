import os
import tempfile
import shutil
from distutils.core import setup
from Cython.Build.Dependencies import cythonize
from multiprocessing import pool


def run_distutils(args):
    base_dir, ext_modules = args
    script_args = ['build_ext', '-i']
    cwd = os.getcwd()
    temp_dir = None
    try:
        if base_dir:
            os.chdir(base_dir)
            temp_dir = tempfile.mkdtemp(dir=base_dir)
            script_args.extend(['--build-temp', temp_dir])
            setup(
                script_name='setup.py',
                script_args=script_args,
                ext_modules=ext_modules,
            )
    finally:
        if base_dir:
            os.chdir(cwd)
            if temp_dir and os.path.isdir(temp_dir):
                shutil.rmtree(temp_dir)


if __name__ == "__main__":
    ext_paths = ['demo.py','additional.py','subfun.py']
    cython_exts = cythonize(ext_paths,
                            nthreads=1,
                            compiler_directives={
                                "always_allow_keywords": False,
                            })
    try:
        process_pool = pool.Pool()
        process_pool.map_async(run_distutils, [(".", [ext]) for ext in cython_exts])
    except:
        if process_pool is not None:
            process_pool.terminate()
        raise
    finally:
        if process_pool is not None:
            process_pool.close()
            process_pool.join()
