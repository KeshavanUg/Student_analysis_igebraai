import React, { useState } from 'react';
import { Student } from './types';

type Props = { students: Student[] };
export default function StudentTable({ students }: Props) {
  const [search, setSearch] = useState('');
  const [sortKey, setSortKey] = useState('assessment_score');
  const [sortOrder, setSortOrder] = useState('desc');

  const filtered = students.filter((s: Student) =>
    s.name.toLowerCase().includes(search.toLowerCase()) ||
    s.class.toString().includes(search)
  );

  const sorted = [...filtered].sort((a: Student, b: Student) => {
    if (sortOrder === 'asc') return (a[sortKey as keyof Student] as number) - (b[sortKey as keyof Student] as number);
    return (b[sortKey as keyof Student] as number) - (a[sortKey as keyof Student] as number);
  });

  return (
    <div className="mt-8">
      <input
        className="border p-2 mb-4 w-full"
        placeholder="Search by name or class..."
        value={search}
        onChange={e => setSearch(e.target.value)}
      />
      <table className="min-w-full bg-white rounded shadow">
        <thead>
          <tr>
            {(Object.keys(sorted[0] || {}) as (keyof Student)[]).map(key => (
              <th key={key} className="p-2 cursor-pointer" onClick={() => setSortKey(key as string)}>{String(key).replace('_',' ')}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {sorted.map(s => (
            <tr key={s.student_id}>
              {(Object.keys(s) as (keyof Student)[]).map(key => (
                <td key={key} className="p-2 border-t">{s[key]}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
