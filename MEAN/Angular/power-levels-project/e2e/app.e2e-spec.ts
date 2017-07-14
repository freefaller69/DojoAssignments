import { PowerLevelsProjectPage } from './app.po';

describe('power-levels-project App', () => {
  let page: PowerLevelsProjectPage;

  beforeEach(() => {
    page = new PowerLevelsProjectPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
