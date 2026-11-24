import sys, asyncio
from playwright.async_api import async_playwright
async def main(site, pages):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        for w,h in [(390,844),(1440,900)]:
            pg = await b.new_page(viewport={"width":w,"height":h})
            for path in pages:
                await pg.goto(f"file:///home/claude/sites/preview/{site}/{path}index.html")
                await pg.wait_for_timeout(300)
                sw = await pg.evaluate("document.documentElement.scrollWidth")
                name = (path.strip('/') or 'home').replace('/','_')
                await pg.screenshot(path=f"shots/{site}_{name}_{w}.png", full_page=True)
                print(site, name, w, "scrollWidth", sw)
        await b.close()
site=sys.argv[1]; pages=sys.argv[2:]
asyncio.run(main(site,pages))
