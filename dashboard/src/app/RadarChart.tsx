import React from 'react';
import { Radar } from 'react-chartjs-2';
import { Chart, RadialLinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';
import { Student } from './types';

Chart.register(RadialLinearScale, PointElement, LineElement, Title, Tooltip, Legend);

export default function RadarChart({ student }: { student: Student }) {
  const data = {
    labels: ['Comprehension', 'Attention', 'Focus', 'Retention', 'Engagement Time', 'Assessment Score'],
    datasets: [
      {
        label: student.name,
        data: [
          student.comprehension,
          student.attention,
          student.focus,
          student.retention,
          student.engagement_time,
          student.assessment_score,
        ],
        backgroundColor: 'rgba(59,130,246,0.2)',
        borderColor: 'rgba(59,130,246,1)',
        pointBackgroundColor: 'rgba(59,130,246,1)',
      },
    ],
  };
  return (
    <div className="bg-white rounded shadow p-4 mb-8">
      <h2 className="text-lg font-bold mb-2">Student Profile (Radar Chart)</h2>
      <Radar data={data} />
    </div>
  );
}
