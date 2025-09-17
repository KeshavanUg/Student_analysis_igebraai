import { Student } from './types';
import studentsData from './students_processed.json';

export const students: Student[] = (studentsData as any[]).map(s => ({
	student_id: Number(s.student_id),
	name: s.name,
	class: Number(s.class),
	comprehension: Number(s.comprehension),
	attention: Number(s.attention),
	focus: Number(s.focus),
	retention: Number(s.retention),
	assessment_score: Number(s.assessment_score),
	engagement_time: Number(s.engagement_time),
	persona: Number(s.persona)
}));
