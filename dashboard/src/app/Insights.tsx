import React from 'react';

export default function Insights() {
  return (
    <section className="bg-gray-50 rounded shadow p-6 mt-8">
      <h2 className="text-xl font-bold mb-2">Insights & Key Findings</h2>
      <ul className="list-disc ml-6">
        <li>Cognitive skills show strong correlation with assessment scores.</li>
        <li>ML model predicts scores accurately for synthetic data.</li>
        <li>Students grouped into three learning personas.</li>
        <li>Personas can help tailor learning strategies.</li>
      </ul>
    </section>
  );
}
