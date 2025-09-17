import React from 'react';
import { Student } from './types';

type Props = { students: Student[] };
export default function OverviewStats({ students }: Props) {
  const avg = (key: keyof Student) => (
    students.length
      ? (
          students.reduce((a, b) => a + Number(b[key]), 0) / students.length
        ).toFixed(2)
      : 0
  );
  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
      <div className="bg-white rounded shadow p-4">
        <h3 className="font-bold">Avg Score</h3>
        <p>{avg('assessment_score')}</p>
      </div>
      <div className="bg-white rounded shadow p-4">
        <h3 className="font-bold">Avg Comprehension</h3>
        <p>{avg('comprehension')}</p>
      </div>
      <div className="bg-white rounded shadow p-4">
        <h3 className="font-bold">Avg Attention</h3>
        <p>{avg('attention')}</p>
      </div>
      <div className="bg-white rounded shadow p-4">
        <h3 className="font-bold">Avg Focus</h3>
        <p>{avg('focus')}</p>
      </div>
    </div>
  );
}
