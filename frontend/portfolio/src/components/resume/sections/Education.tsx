import { EntryBlock } from "../ui/EntryBlock";
import { SectionBlock } from "../ui/SectionBlock";

export function Education() {
  return (
    <SectionBlock title="Education">
      <EntryBlock
        title="Masters of Applied Computer Science"
        subtitle="Dalhousie University"
        location="Halifax, NS"
        startDate={new Date(2023, 4)}
        endDate={new Date(2024, 7)}
      />
      <EntryBlock
        title="Graduate Certificate program (Computer Science)"
        subtitle="University of Florida"
        location="Gainesville, FL, USA"
        startDate={new Date(2020, 0)}
        endDate={new Date(2020, 4)}
      />
      <EntryBlock
        title="Bachelors in technology (Computer Science & Engineering)"
        subtitle="Manipal University Jaipur"
        location="Jaipur, RJ, India"
        startDate={new Date(2016, 7)}
        endDate={new Date(2020, 9)}
      />
    </SectionBlock>
  );
}
