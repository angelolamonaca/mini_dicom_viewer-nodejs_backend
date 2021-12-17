'use strict';
module.exports = {
    up: async (queryInterface, Sequelize) => {
        await queryInterface.createTable('Studies', {
            id: {
                allowNull: false,
                autoIncrement: true,
                primaryKey: true,
                type: Sequelize.INTEGER
            },
            idPatient: {
                type: Sequelize.INTEGER,
                references: {
                    model: {
                        tableName: 'Patients',
                    },
                    key: 'id',
                },
              onUpdate: 'CASCADE',
              onDelete: 'CASCADE',
            },
            studyName: {
                type: Sequelize.STRING
            },
            createdAt: {
                allowNull: false,
                type: Sequelize.DATE
            },
            updatedAt: {
                allowNull: false,
                type: Sequelize.DATE
            }
        });
    },
    down: async (queryInterface, Sequelize) => {
        await queryInterface.dropTable('Studies');
    }
};