const patientResolver = require('./patient');
const studyResolver = require('./study');
const seriesResolver = require('./series');
const modalityResolver = require('./modality');
const fileResolver = require('./file');
module.exports = [patientResolver, studyResolver, seriesResolver, modalityResolver, fileResolver];