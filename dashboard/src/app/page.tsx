import { students } from './data';
import OverviewStats from './OverviewStats';
import StudentTable from './StudentTable';

import BarChart from './BarChart';
import Insights from './Insights';
import ScatterChart from './ScatterChart';
import RadarChart from './RadarChart';

export default function Home() {
  return (
    <div className="font-sans min-h-screen p-8 pb-20 bg-gray-100">
      <h1 className="text-3xl font-bold mb-8 text-center">Cognitive Skills & Student Performance Dashboard</h1>
  <OverviewStats students={students} />
  <BarChart students={students} />
  <ScatterChart students={students} />
  <RadarChart student={students[0]} />
  <StudentTable students={students} />
  <Insights />
    </div>
  );
}
