# Content Analyzer Enhancement - File Upload & Performance Assessment

## Overview
The Content Analyzer feature has been significantly enhanced to support file uploads (PDF, DOCX, TXT) and test performance assessment functionality.

## New Features

### 1. **File Upload Support** 📁
Upload educational materials in multiple formats for analysis:
- **Supported Formats:** PDF, DOCX, DOC, TXT
- **Drag & Drop:** Click or drag files to upload area
- **File Validation:** Automatic file type checking
- **Error Handling:** Clear error messages for unsupported formats

### 2. **Test Performance Assessment** 📊
New analysis type for evaluating test/quiz performance:
- **Input:** Number of questions answered vs. total questions
- **Output:** 
  - Score percentage calculation
  - Performance feedback
  - Areas of strength
  - Areas needing improvement
  - Specific study recommendations
  - Encouragement and motivational guidance

### 3. **Dynamic Form UI**
- Shows performance section only when "Assess Test Performance" is selected
- Real-time score calculation (shows percentage and ratio)
- Visual indicators for performance metrics

## Technical Implementation

### Files Modified/Created

**Frontend:**
- `frontend/ai-tools.html` - Added file upload UI and performance section
- `frontend/js/ai-tools.js` - Enhanced with:
  - File drag & drop handling
  - File validation
  - Real-time score calculation
  - Dual submission paths (file vs. text)
- `frontend/css/ai-tools.css` - New file with upload and performance styling

**Backend:**
- `backend/routes/ai_tools_routes.py` - Updated to handle multipart form data
- `backend/services/ai_service.py` - Added:
  - `extract_text_from_file()` - Extracts text from various file formats
  - Enhanced `analyze_content()` with performance parameters
  - Enhanced `generate_fallback_analysis()` with assessment support
- `backend/requirements.txt` - Added dependencies:
  - `python-docx` - For DOCX file handling
  - `PyPDF2` - For PDF file handling

## API Endpoints

### File Upload Analysis
**POST** `/api/analyze-content` (multipart/form-data)

**Request:**
```
file: <File object>
analysisType: "assessment" | "summary" | "explain" | "keypoints" | "questions"
detailLevel: "Brief" | "Detailed" | "Comprehensive"
questionsAnswered: integer (optional, for assessment type)
totalQuestions: integer (optional, for assessment type)
```

**Response:**
```json
{
  "success": true,
  "analysisType": "assessment",
  "analysis": "Detailed analysis with performance feedback..."
}
```

### Text Content Analysis (Existing, Enhanced)
**POST** `/api/analyze-content` (application/json)

**Request:**
```json
{
  "content": "Text content here...",
  "analysisType": "assessment",
  "detailLevel": "Detailed",
  "questionsAnswered": 8,
  "totalQuestions": 10
}
```

## File Format Support

### PDF Files
- Uses PyPDF2 library
- Extracts text from all pages
- Handles multi-page documents
- Error handling for corrupted files

### DOCX/DOC Files
- Uses python-docx library
- Extracts text from all paragraphs
- Preserves document structure
- Supports modern Word formats

### TXT Files
- Direct text extraction
- UTF-8 encoding support
- Simple and reliable

## Assessment Feature Details

### Score Calculation
```
Score % = (Questions Answered / Total Questions) × 100
```

### Performance Levels
- **90-100%:** Excellent! Outstanding performance!
- **80-89%:** Very Good! Strong understanding demonstrated.
- **70-79%:** Good! Solid grasp of the material.
- **60-69%:** Satisfactory. Some areas need improvement.
- **Below 60%:** Needs Improvement. Consider reviewing the material.

### Feedback Components
1. **Your Score** - Clear display of percentage and ratio
2. **Performance Summary** - Overall assessment
3. **What You Did Well** - Areas of mastery
4. **Areas for Improvement** - Specific weak points
5. **Recommendations** - Actionable steps to improve
6. **Next Steps** - Long-term learning strategy
7. **Encouragement** - Motivational message

## Error Handling

### Frontend Validation
- File type validation
- File size indication
- Clear error messages
- Input requirement checks

### Backend Validation
- File format verification
- Content length validation (minimum 10 characters)
- Exception handling with detailed logging
- Fallback responses when API unavailable

## Fallback Mode
When Groq API is unavailable:
- **Regular Analysis:** Basic template-based analysis
- **Assessment:** Generates encouraging feedback with:
  - Score calculation
  - Performance interpretation
  - General improvement suggestions
  - Study tips

## Usage Examples

### Example 1: Upload Quiz PDF
1. Click "Upload File (PDF, DOCX, TXT)"
2. Select a quiz PDF
3. Choose "Assess Test Performance"
4. Enter "8" for Questions Answered
5. Enter "10" for Total Questions
6. See real-time score: "80% (8/10)"
7. Click "Analyze Content"
8. Receive detailed performance feedback

### Example 2: Paste and Analyze Text
1. Select analysis type (e.g., "Summarize Content")
2. Paste content directly
3. Choose detail level
4. Click "Analyze Content"
5. Get AI-powered analysis
6. Copy results to clipboard

## Installation & Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- `python-docx` - Document handling
- `PyPDF2` - PDF processing
- Other existing dependencies

### 2. Environment Configuration
Ensure `.env` contains:
```
GROQ_API_KEY=your_api_key_here
```

### 3. Restart Flask Server
```bash
python app.py
```

## Browser Compatibility
- Modern browsers with FormData support
- File API support
- Fetch API with multipart handling
- Works on desktop and mobile

## Security Considerations
- File type validation on client and server
- Content length validation
- Error messages don't expose sensitive paths
- Temporary files are not persisted
- No file storage - all processing is in-memory

## Performance Optimizations
- Client-side file type validation before upload
- Real-time score calculation without server call
- Streaming text extraction for large files
- Efficient memory usage with form data

## Future Enhancements
- Support for more file formats (.pptx, .xlsx, etc.)
- Batch file upload
- Answer key comparison for assessments
- Detailed question-by-question analysis
- Performance tracking over time
- Export assessment reports as PDF
- Multiple language support
- OCR for scanned documents

## Troubleshooting

### "PDF support not available"
- Install PyPDF2: `pip install PyPDF2`
- Restart Flask server

### "DOCX support not available"
- Install python-docx: `pip install python-docx`
- Restart Flask server

### File upload not working
- Check browser console for errors
- Verify file format is supported
- Ensure file isn't corrupted
- Check file size isn't excessive

### Analysis taking too long
- Large files take longer to process
- PDF with images takes longer than text-only
- Check internet connection for API calls
- Try with shorter content

## Code Examples

### Client-Side: Handle File Upload
```javascript
const formData = new FormData();
formData.append('file', fileInput.files[0]);
formData.append('analysisType', 'assessment');
formData.append('questionsAnswered', 8);
formData.append('totalQuestions', 10);

const response = await fetch('/api/analyze-content', {
  method: 'POST',
  body: formData
});
```

### Server-Side: Extract Text
```python
from services.ai_service import extract_text_from_file

text = extract_text_from_file(file_obj)
analysis = analyze_content(
    content=text,
    analysis_type='assessment',
    questions_answered=8,
    total_questions=10
)
```

## Conclusion
The enhanced Content Analyzer now provides a comprehensive solution for analyzing educational materials in multiple formats and assessing student performance with personalized, actionable feedback.
