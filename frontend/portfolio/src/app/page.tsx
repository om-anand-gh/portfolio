import { Education } from "@/components/resume/sections/Education";
import { WorkExperience } from "@/components/resume/sections/WorkExperience";
import { Card, CardContent } from "@/components/ui/card";

export default function Home() {
  return (
    <div>
      <section className="mx-auto mt-12 max-w-3xl space-y-6 px-8">
        {/* Personal Intro */}
        <div className="space-y-2">
          <h1 className="text-4xl font-bold">Om Anand</h1>
          <p className="text-muted-foreground text-lg">
            Full-stack engineer specializing in scalable infrastructure, clean
            APIs, and product-driven development across the cloud.
          </p>
        </div>

        {/* Work in Progress Notice */}
        <p className="rounded-md border border-yellow-400 bg-yellow-100 p-4 text-yellow-900">
          🚧 Work in progress — this resume is still under construction! Check
          back soon for the magic.
        </p>

        {/* Resume Content */}
        <Card>
          <CardContent className="space-y-6 py-6">
            <WorkExperience />
            <Education />
          </CardContent>
        </Card>
      </section>
    </div>
  );
}
