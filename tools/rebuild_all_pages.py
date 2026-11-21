import os
import sys

# Ensure tools directory is in sys.path
tools_dir = os.path.dirname(os.path.abspath(__file__))
if tools_dir not in sys.path:
    sys.path.insert(0, tools_dir)

from build_helpers import get_page_shell, make_placeholder
import generate_pages_part1
import build_services_pages
import build_services_individual
import build_corp_pages
import build_final_pages

print("Starting complete rebuild of all 31 HTML pages with new color themes...")

# 1. Homepage
generate_pages_part1.build_index()

# 2. About & Services Overview
build_services_pages.build_about()
build_services_pages.build_services_overview()

# 3. 13 Practice Pages (Pages 4 to 16)
build_services_individual.generate_individual_services()

# 4. Corporate & Resource Pages (Pages 17 to 24)
build_corp_pages.generate_corp_pages()

# 5. Final Pages (Pages 25 to 31)
build_final_pages.generate_final_pages()

print("Rebuild of all 31 pages completed successfully!")
