# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '法奥文档'
# project = 'FRROSPlatform'
copyright = 'Copyright 2022, 法奥意威（苏州）机器人系统有限公司'
# copyright = 'Copyright 2022, Fair Innovation (Suzhou) Robotic System Co.,Ltd.'
author = 'Zhao Jinqi'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['recommonmark']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'
locale_dirs = ['../locale/']  # 设置本地化数据目录

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


highlight_language = "c,c++,python"