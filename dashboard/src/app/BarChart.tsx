import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Student } from './types';

export default function BarChart({ students }: { students: Student[] }) {
  const data = {
    labels: students.map(s => s.name),
    datasets: [
      {
        label: 'Assessment Score',
        data: students.map(s => s.assessment_score),
        backgroundColor: 'rgba(59,130,246,0.6)',
      },
      {
        label: 'Comprehension',
        data: students.map(s => s.comprehension),
        backgroundColor: 'rgba(16,185,129,0.6)',
      },
      {
        label: 'Attention',
        data: students.map(s => s.attention),
        backgroundColor: 'rgba(234,179,8,0.6)',
      },
      {
        label: 'Focus',
        data: students.map(s => s.focus),
        backgroundColor: 'rgba(239,68,68,0.6)',
      },
    ],
  };
  return (
    <div className="bg-white rounded shadow p-4 mb-8">
      <h2 className="text-lg font-bold mb-2">Skill vs Score (Bar Chart)</h2>
      <Bar data={data} />
    </div>
  );
}
