namespace devtests;

public class HiveManagementTests
{
    [Fact]
    public void ListAllHives()
    {
        var apriary = ApriaryStorage.load();
        var hives = apriary.Hives;

        hives.Should().HaveCount(4, "Hard coded initial hives list");
    }
}