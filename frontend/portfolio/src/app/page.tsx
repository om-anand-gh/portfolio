import {
  NavigationMenu,
  NavigationMenuList,
  NavigationMenuItem,
  NavigationMenuLink,
} from "@/components/ui/navigation-menu";
import { ModeToggle } from "@/components/ModeToggle";

export default function Home() {
  return (
    <div>
      <main className="min-h-screen p-8">
        <header className="flex items-center justify-between">
          <NavigationMenu>
            <NavigationMenuList>
              <NavigationMenuItem>
                <NavigationMenuLink href="/">Home</NavigationMenuLink>
              </NavigationMenuItem>
              <NavigationMenuItem>
                <NavigationMenuLink href="https://linkedin.com/in/om-anand/">
                  LinkedIn
                </NavigationMenuLink>
              </NavigationMenuItem>
              <NavigationMenuItem>
                <NavigationMenuLink href="https://github.com/om-anand-gh">
                  Github
                </NavigationMenuLink>
              </NavigationMenuItem>
            </NavigationMenuList>
          </NavigationMenu>
          <ModeToggle />
        </header>

        <section className="mt-12 space-y-4">
          <h1 className="text-4xl font-bold">Welcome to My Portfolio</h1>
          <p>
            {" "}
            🚧 Work in progress - my resume is still under construction! Check
            back soon for the magic.{" "}
          </p>
        </section>
      </main>
    </div>
  );
}
