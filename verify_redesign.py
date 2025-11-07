
import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Get the absolute path to the HTML file
        file_path = os.path.abspath('ttrpg_random_gen_V106.html')

        # Go to the local HTML file
        await page.goto(f'file://{file_path}')

        # 1. Verify Home Screen Redesign
        await page.screenshot(path='screenshot_home.png')

        # 2. Verify "More..." dropdown
        await page.hover('button:has-text("More...")')
        await page.screenshot(path='screenshot_more_dropdown.png')

        # 3. Verify Table Card Context Menu
        # Ensure there is at least one table to hover over
        if await page.query_selector('.table-item'):
            await page.hover('.table-item')
            # The dropdown is part of the table item, so we need to hover over the button specifically
            await page.hover('.table-item .dropdown-toggle')
            await page.screenshot(path='screenshot_table_context_menu.png')

        # 4. Verify Single-Table View (collapsible entries)
        if await page.query_selector('.table-item'):
            await page.click('.table-item')
            # Wait for the view to change
            await page.wait_for_selector('#tableView:not(.hidden)')
            # Ensure the details/summary element exists before clicking
            if await page.query_selector('#tableView details summary'):
                await page.click('#tableView details summary') # Click to expand
            await page.screenshot(path='screenshot_table_view_expanded.png')
            if await page.query_selector('#tableView details summary'):
                await page.click('#tableView details summary') # Click to collapse
            await page.screenshot(path='screenshot_table_view_collapsed.png')
            await page.click('button:has-text("← Back")')
            await page.wait_for_selector('#homeView:not(.hidden)')


        # 5. Verify Select Mode and Multi-Select Bar
        await page.click('button:has-text("Select")')
        await page.wait_for_selector('.table-select-checkbox', state='visible')
        await page.screenshot(path='screenshot_select_mode_on.png')

        if await page.query_selector('.table-item'):
            await page.click('.table-item .table-select-checkbox')

        await page.wait_for_selector('#multiSelectBar.active', state='visible')
        await page.screenshot(path='screenshot_multi_select_bar.png')

        await page.click('button:has-text("Cancel")')
        await page.wait_for_selector('#multiSelectBar:not(.active)', state='hidden')
        await page.screenshot(path='screenshot_select_mode_off.png')

        await browser.close()

asyncio.run(main())
