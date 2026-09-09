from pathlib import Path


REPORT_DIR = Path("reports")
SCREENSHOT_DIR = REPORT_DIR / "screenshots"


def create_report_directories():
    REPORT_DIR.mkdir(exist_ok=True)
    SCREENSHOT_DIR.mkdir(exist_ok=True)


def take_screenshot(page, name):
    create_report_directories()

    screenshot_path = SCREENSHOT_DIR / f"{name}.png"

    page.screenshot(
        path=str(screenshot_path),
        full_page=True
    )

    return str(screenshot_path)