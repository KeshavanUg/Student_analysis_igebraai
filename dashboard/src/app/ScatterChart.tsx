import React from 'react';
import { Scatter } from 'react-chartjs-2';
import { Chart, PointElement, LinearScale, Title, Tooltip, Legend } from 'chart.js';
import { Student } from './types';

Chart.register(PointElement, LinearScale, Title, Tooltip, Legend);

export default function ScatterChart({ students }: { students: Student[] }) {
  const data = {
    datasets: [
      {
        label: 'Attention vs Assessment Score',
        data: students.map(s => ({ x: s.attention, y: s.assessment_score })),
        backgroundColor: 'rgba(59,130,246,0.7)',
      },
    ],
  };
  const options = {
    scales: {
      x: { title: { display: true, text: 'Attention' } },
      y: { title: { display: true, text: 'Assessment Score' } },
    },
  };
  return (
    <div className="bg-white rounded shadow p-4 mb-8">
      <h2 className="text-lg font-bold mb-2">Attention vs Performance (Scatter Chart)</h2>
      <Scatter data={data} options={options} />
    </div>
  );
}
