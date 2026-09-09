from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.set_default_timeout(10000)
    page.goto("https://www.saucedemo.com/")
    print("Title:", page.title())

    # Login
    page.locator("#user-name").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    # Verify login
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page).to_have_title("Swag Labs")
    expect(page.get_by_text("Products")).to_be_visible()

    # Sort products
    page.locator("[data-test='product-sort-container']").select_option("lohi")

    buttons = page.get_by_role("button",name="Add to cart")
    print(buttons.count())
    #page.get_by_role("button",name="Add to cart").first.click()
    #page.get_by_role("button",name="Add to cart").last.click()
    #page.get_by_role("button",name="Add to cart").nth(2).click()
    
    # Find Backpack
    product = page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")

    # Add Backpack to cart
    product.get_by_role("button",name="Add to cart").click()
    

    # Verify cart
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    input("Press Enter to close the browser...")
    browser.close()
    
    


