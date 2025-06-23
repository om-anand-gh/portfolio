import { Button } from "@/components/ui/button";
import {
  NavigationMenu,
  NavigationMenuList,
  NavigationMenuItem,
  NavigationMenuLink,
} from "@/components/ui/navigation-menu";
import { ModeToggle } from "@/components/ModeToggle";
import { GithubLogoIcon, LinkedinLogoIcon } from "@/assets/icons";

export function Header() {
  return (
    <header className="sticky top-0 z-50 bg-white dark:bg-black flex items-center justify-between px-4 py-2 shadow-sm">
      <NavigationMenu>
        <NavigationMenuList>
          <NavigationMenuItem>
            <NavigationMenuLink href="/">Home</NavigationMenuLink>
          </NavigationMenuItem>
        </NavigationMenuList>
      </NavigationMenu>
      {/* Right-side icons */}
      <div className="ml-auto flex items-center space-x-2">
        <Button asChild aria-label="GitHub" variant="outline">
          <a
            href="https://github.com/om-anand-gh"
            target="_blank"
            rel="noopener noreferrer"
          >
            <GithubLogoIcon size={24} />
          </a>
        </Button>
        <Button asChild aria-label="LinkedIn" variant="outline">
          <a
            href="https://www.linkedin.com/in/om-anand"
            target="_blank"
            rel="noopener noreferrer"
          >
            <LinkedinLogoIcon size={24} />
          </a>
        </Button>
        <ModeToggle />
      </div>
    </header>
  );
}
