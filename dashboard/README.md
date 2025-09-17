
# Cognitive Skills & Student Performance Dashboard

This project analyzes synthetic student data and visualizes cognitive skills and performance using a Next.js dashboard.

## Features
- Overview stats (average scores and skills)
- Bar chart: Skill vs Score
- Scatter chart: Attention vs Performance
- Radar chart: Student Profile
- Searchable/sortable student table
- Insights section with key findings

## Setup Instructions
1. **Install dependencies:**
	```bash
	npm install
	```
2. **Run the dashboard locally:**
	```bash
	npm run dev
	```
	Open [http://localhost:3000](http://localhost:3000) in your browser.

3. **Data Source:**
	- The dashboard uses `students_processed.json` in `src/app` (converted from your notebook output).

## Deployment
- Deploy to Vercel for a public link: [https://vercel.com/](https://vercel.com/)
- Connect your GitHub repo and follow Vercel instructions.

## Key Findings
- Cognitive skills strongly correlate with assessment scores.
- ML model predicts scores accurately for synthetic data.
- Students grouped into three learning personas.
- Personas can help tailor learning strategies.

## Deliverables
- Jupyter Notebook (analysis + ML)
- Next.js dashboard (visualizations + table)
- GitHub repo with code
- Deployed Vercel link (publicly shareable)
- README (setup + findings)

---
For any issues, check your data file and dependencies, or contact your instructor.
