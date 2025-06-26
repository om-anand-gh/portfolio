import { BulletItem } from "../ui/BulletItem";
import { EntryBlock } from "../ui/EntryBlock";
import { EntryContent } from "../ui/EntryContent";
import { SectionBlock } from "../ui/SectionBlock";

export function WorkExperience() {
  return (
    <SectionBlock title="Work Experience">
      <EntryBlock
        title="Software Engineer"
        subtitle="Scient Analytics"
        location="Remote (Halifax, NS) + Travel (ON)"
        startDate={new Date(2024, 0)}
      >
        <EntryContent>
          <BulletItem>Azure Architect</BulletItem>
          <BulletItem>Django Developer</BulletItem>
          <BulletItem>React Refactorer</BulletItem>
        </EntryContent>
      </EntryBlock>
      <EntryBlock
        title="Teaching Assitant - Cloud Architecture"
        subtitle="Dalhousie University"
        location="Halifax, NS"
        startDate={new Date(2024, 4)}
        endDate={new Date(2024, 11)}
      >
        <EntryContent>
          <BulletItem>AWS-Azure Architect</BulletItem>
        </EntryContent>
      </EntryBlock>
      <EntryBlock
        title="Teaching Assitant - Workplace Communication for CS"
        subtitle="Dalhousie University"
        location="Halifax, NS"
        startDate={new Date(2023, 8)}
        endDate={new Date(2024, 3)}
      >
        <EntryContent>
          <BulletItem>Communication Connoisseur</BulletItem>
        </EntryContent>
      </EntryBlock>
      <EntryBlock
        title="Test Automation Engineer"
        subtitle="Tata Consultancy Services"
        location="Hyderabad, TS, India"
        startDate={new Date(2020, 9)}
        endDate={new Date(2022, 10)}
      >
        <EntryContent>
          <BulletItem>CI/CD Controller</BulletItem>
          <BulletItem>Test Tattler</BulletItem>
        </EntryContent>
      </EntryBlock>
      <EntryBlock
        title="Academic Intern"
        subtitle="National University of Singapore"
        location="Kent Ridge, Singapore"
        startDate={new Date(2018, 5)}
        endDate={new Date(2018, 6)}
      >
        <EntryContent>
          <BulletItem>Big Data Battler</BulletItem>
          <BulletItem>Spark Sprinter</BulletItem>
        </EntryContent>
      </EntryBlock>
    </SectionBlock>
  );
}
