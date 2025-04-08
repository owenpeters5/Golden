let currentDate = new Date();

function formatDate(date) {
    return date.toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric'
    });
}

function getWeekDates(date) {
    const start = new Date(date);
    start.setDate(start.getDate() - start.getDay());
    
    const dates = [];
    for (let i = 0; i < 7; i++) {
        const day = new Date(start);
        day.setDate(start.getDate() + i);
        dates.push(day);
    }
    return dates;
}

function updateCalendar() {
    const weekDates = getWeekDates(currentDate);
    const calendarBody = document.getElementById('calendar-body');
    calendarBody.innerHTML = '';
    
    const today = new Date();
    
    weekDates.forEach(date => {
        const cell = document.createElement('div');
        cell.className = 'calendar-cell';
        
        if (date.toDateString() === today.toDateString()) {
            cell.className += ' today';
        }
        
        const dateDiv = document.createElement('div');
        dateDiv.className = 'calendar-date';
        dateDiv.textContent = formatDate(date);
        
        cell.appendChild(dateDiv);
        calendarBody.appendChild(cell);
    });

    // Update header
    const firstDay = weekDates[0];
    const lastDay = weekDates[6];
    document.getElementById('currentWeek').textContent = 
        `${formatDate(firstDay)} - ${formatDate(lastDay)}`;
}

function previousWeek() {
    currentDate.setDate(currentDate.getDate() - 7);
    updateCalendar();
}

function nextWeek() {
    currentDate.setDate(currentDate.getDate() + 7);
    updateCalendar();
}

// Initialize calendar when the document is loaded
document.addEventListener('DOMContentLoaded', function() {
    updateCalendar();
}); 