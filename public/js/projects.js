// Guided project catalog shared across pages

window.GuidedProjects = [
  {
    id: 'project-budget-tracker',
    title: 'Personal Budget Tracker',
    difficulty: 'Beginner',
    duration: '2-3 hours',
    subject: 'Python',
    lessonTitle: 'Python Basics: Variables and Data Types',
    summary: 'Build a simple command-line budget tracker that records income and expenses.',
    skills: ['Variables', 'Lists', 'Conditionals'],
    steps: [
      'Define data structures for income and expense entries.',
      'Create prompts to add transactions from user input.',
      'Calculate totals and current balance.',
      'Print a summary report with categories.'
    ],
    deliverables: ['Working script', 'Sample run output', 'Summary report']
  },
  {
    id: 'project-portfolio-page',
    title: 'Portfolio Landing Page',
    difficulty: 'Beginner',
    duration: '3-4 hours',
    subject: 'Web Development',
    lessonTitle: 'HTML Fundamentals',
    summary: 'Design a personal portfolio page with hero, projects, and contact sections.',
    skills: ['HTML structure', 'CSS layout', 'Responsive design'],
    steps: [
      'Sketch a simple layout with header, hero, and sections.',
      'Build the HTML structure with semantic tags.',
      'Style typography, spacing, and colors.',
      'Make it responsive for mobile devices.'
    ],
    deliverables: ['Responsive HTML/CSS page', 'Live preview screenshot', 'Short description']
  },
  {
    id: 'project-quiz-app',
    title: 'Interactive Quiz App',
    difficulty: 'Intermediate',
    duration: '4-5 hours',
    subject: 'JavaScript',
    lessonTitle: 'JavaScript Fundamentals',
    summary: 'Create a multi-question quiz with scoring and feedback.',
    skills: ['DOM events', 'State management', 'User feedback'],
    steps: [
      'Define quiz questions as an array of objects.',
      'Render each question and options to the page.',
      'Capture answers and compute score.',
      'Display feedback and allow retries.'
    ],
    deliverables: ['Working quiz page', 'Score summary', 'Accessible button states']
  },
  {
    id: 'project-ai-brief',
    title: 'AI Ethics Brief',
    difficulty: 'Intermediate',
    duration: '2-3 hours',
    subject: 'Artificial Intelligence',
    lessonTitle: 'What is Artificial Intelligence?',
    summary: 'Write a concise brief analyzing ethical risks for an AI application.',
    skills: ['Research', 'Critical thinking', 'Clear writing'],
    steps: [
      'Choose an AI use-case and describe it clearly.',
      'Identify potential risks and affected groups.',
      'Propose mitigation strategies and safeguards.',
      'Summarize your recommendations in one page.'
    ],
    deliverables: ['One-page brief', 'Risk table', 'Mitigation plan']
  }
];
